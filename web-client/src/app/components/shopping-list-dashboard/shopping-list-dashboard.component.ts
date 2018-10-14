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
    cartArticles = new MatTableDataSource(this.shoppingList);
    allArticles = new MatTableDataSource(this.articles);
    search: {} = {};
    totalOfUnits: {[articleId: string]: number} = {};
    unitsToRemove: {[articleId: string]: number} = {};
    

    storedArticlesColumns: string[] = ['item', 'price', 'units', 'add'];

    listColumns: string[] = ['item', 'cost', 'units', 'total', 'remove'];
    
    @ViewChild(MatPaginator) paginator: MatPaginator;

    
	constructor(
        private articlesService: ArticlesService,
        private shoppingListService: ShoppingListService,
        public dialog: MatDialog
    ) { }
    
    openDialog(article: Article): void {
        this.dialog.open(ArticleComponent, {
            width: '850px',
            data: article
        });
    }
    
    ngOnInit() {
        this.getArticles();
        this.allArticles.paginator = this.paginator;
        this.getCategories();
        this.getShoppingList();
    }
        
    /** Gets the total cost of all transactions. */
    getTotalCost() {
        return this.cartArticles.data.map(t => t[0].price * t[1]).reduce((acc, value) => acc + value, 0);
    }

    applyFilter(filterValue: string) {
        this.allArticles.filter = filterValue.trim().toLocaleLowerCase();
        
        if (this.allArticles.paginator) {
            this.allArticles.paginator.firstPage();
        }
    }


	noArticles(): boolean {
		let emptyArticles: Article[];
		return this.articles == emptyArticles;
	}

	getArticles() {
		this.articlesService.getArticles().subscribe(data => {
            this.articles = data;
            this.allArticles.data = data;
		});
	};

	getCategories() {
		this.articlesService.getCategories().subscribe(data => {
			this.categories = data;
		});
	};

	addCategoryToFilter(categoryId: string) {
		this.articlesService.getSubCategories(categoryId).subscribe(data => {
			this.subcategories = data;
			this.search['category_id'] = categoryId;
            delete this.search['sub_category_id'];
			this.getFilteredArticles();
		});
	};

	addSubCategoryToFilter(subcategoryId: string) {
		this.search['sub_category_id'] = subcategoryId;
		this.getFilteredArticles();
	};

	getFilteredArticles() {
		this.articlesService.getFilteredArticles(this.search)
            .subscribe(data => {
                this.articles = data;
                this.allArticles.data = data;
            });
    };
    
 

	getShoppingList() {
        this.shoppingList = this.shoppingListService.getShoppingList();
	}

	addArticle(article: Article) {
        if (this.totalOfUnits[article.id] == null) {
            this.totalOfUnits[article.id] = 1;
        }
        this.cartArticles.data = this.shoppingListService.addArticle(article, this.totalOfUnits[article.id]);
	}

	removeArticle(article: Article) {
        if (this.unitsToRemove[article.id] == null) {
            this.unitsToRemove[article.id] = this.totalOfUnits[article.id];
        }
        this.cartArticles.data = this.shoppingListService.removeArticle(article, this.unitsToRemove[article.id]);
	}


}
