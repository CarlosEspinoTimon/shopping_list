import { Component, OnInit, ViewChild } from '@angular/core';

import { Article } from '../../models/article';
import { ArticlesService } from '../../services/articles.service';
import { Category}  from '../../models/category';
import { SubCategory}  from '../../models/subcategory';
import { ShoppingListService } from '../../services/shopping-list/shopping-list.service';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';

import { MatDialog, MatPaginator, MatTableDataSource } from '@angular/material';
import { ArticleComponent } from '../article/article.component';



@Component({
	selector: 'app-shopping-list-dashboard',
	templateUrl: './shopping-list-dashboard.component.html',
	styleUrls: ['./shopping-list-dashboard.component.css']
})
export class ShoppingListDashboardComponent implements OnInit {

	articles: Article[];
	categories: Category[];
    subcategories: SubCategory[];
    shoppingList: [[Article, number]];
    searchPassedToServer: {} = {};
    totalOfUnits: {[articleId: string]: number} = {};
    unitsToRemove: {[articleId: string]: number} = {};
    
    allArticles = new MatTableDataSource(this.articles);
    cartArticles = new MatTableDataSource(this.shoppingList);
    // Columns for mat tables
    storedArticlesColumns: string[] = ['item', 'price', 'units', 'add'];
    listColumns: string[] = ['item', 'cost', 'units', 'total', 'remove'];
    
    @ViewChild(MatPaginator) paginator: MatPaginator;

    
	constructor(
        private articlesService: ArticlesService,
        private shoppingListService: ShoppingListService,
        public dialog: MatDialog
    ) { }
    
    ngOnInit() {
        this.getArticles();
        this.allArticles.paginator = this.paginator;
        this.getCategories();
        this.getShoppingList();
    }
    
    /** Modal that opens with article info. */
    openDialog(article: Article): void {
        this.dialog.open(ArticleComponent, {
            width: '850px',
            data: article
        });
    }
    

    /** Gets the total cost of all transactions. */
    getTotalCost() {
        return this.cartArticles.data.map(t => t[0].price * t[1]).reduce((acc, value) => acc + value, 0);
    }

    /** Filter applied to elements of the mat table. */
    applyFilter(filterValue: string) {
        this.allArticles.filter = filterValue.trim().toLocaleLowerCase();
        
        if (this.allArticles.paginator) {
            this.allArticles.paginator.firstPage();
        }
    }

    /** Function that checks if there are articles already loaded */
	noArticles(): boolean {
		let emptyArticles: Article[];
		return this.articles == emptyArticles;
	}

    /** Function that gets all the articles */
	getArticles() {
		this.articlesService.getArticles().subscribe(data => {
            this.allArticles.data = data;
		});
	};

    /** Function that gets all the Categories */
	getCategories() {
		this.articlesService.getCategories().subscribe(data => {
			this.categories = data;
		});
	};

    /** Function that adds the choosen Category to the server filter and gets all
     * the products for this Caterory and its Subcategories 
     */
	addCategoryToFilter(categoryId: string) {
		this.articlesService.getSubCategories(categoryId).subscribe(data => {
			this.subcategories = data;
            this.searchPassedToServer['category_id'] = categoryId;
            // Remove old subcategory serch
            delete this.searchPassedToServer['sub_category_id'];
			this.getFilteredArticles();
		});
	};

    /** Function that adds the choosen SubCategory to the server and getsa all the
     * products from this SubCategory
     */
	addSubCategoryToFilter(subcategoryId: string) {
		this.searchPassedToServer['sub_category_id'] = subcategoryId;
		this.getFilteredArticles();
	};

    /** Function that gets all the articles with the filters already choosen */
	getFilteredArticles() {
		this.articlesService.getFilteredArticles(this.searchPassedToServer)
            .subscribe(data => {
                this.allArticles.data = data;
            });
    };
    
 
    /** Function that returns the shopping list */
	getShoppingList() {
        this.shoppingList = this.shoppingListService.getShoppingList();
	}

    /** Functions that adds a new article */
	addArticle(article: Article) {
        if (this.totalOfUnits[article.id] == null) {
            this.totalOfUnits[article.id] = 1;
        }
        this.cartArticles.data = this.shoppingListService.addArticle(article, this.totalOfUnits[article.id]);
        if (this.unitsToRemove[article.id] == null) {
            this.unitsToRemove[article.id] = this.totalOfUnits[article.id];
        } else {
            this.unitsToRemove[article.id] = this.unitsToRemove[article.id] + this.totalOfUnits[article.id];
        }
	}

    /** Functions that removes an article */
	removeArticle(article: Article) {
        this.cartArticles.data = this.shoppingListService.removeArticle(article, this.unitsToRemove[article.id]);
	}


}
