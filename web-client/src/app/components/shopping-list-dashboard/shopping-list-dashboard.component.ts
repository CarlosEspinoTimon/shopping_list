import { Component, OnInit, Inject } from '@angular/core';

import { Article } from '../../models/article';
import { ArticlesService } from '../../services/articles.service';
import { Category}  from '../../models/category';
import { SubCategory}  from '../../models/subcategory';
import { ShoppingListService } from '../../services/shopping-list/shopping-list.service';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';

import { MatDialog } from '@angular/material';
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
	shoppingList: Article[];
    search: {} = {};
    myControl = new FormControl();
    filteredArticles: Observable<Article[]>;



	constructor(
		private articlesService: ArticlesService,
        private shoppingListService: ShoppingListService,
        public dialog: MatDialog
    ) { }

    openDialog(article: Article): void {
        const dialogRef = this.dialog.open(ArticleComponent, {
            width: '850px',
            data: article
        });
      }

	ngOnInit() {
		this.getArticles();
        this.getCategories();
    }
    
    private _filter(value: string): Article[] {
        const filterValue = value.toLocaleLowerCase();
        return this.articles.filter(option => option.name.toLowerCase().includes(filterValue));
    }

	noArticles(): boolean {
		let emptyArticles: Article[];
		return this.articles == emptyArticles;
	}

	getArticles() {
		this.articlesService.getArticles().subscribe(data => {
            this.articles = data;
            this.changeArticlesToShow();
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
                this.changeArticlesToShow();
            });
    };
    
    changeArticlesToShow() {
        this.filteredArticles = this.myControl.valueChanges
                .pipe(
                    startWith(''),
                    map(value => this._filter(value))
                );
    }

	getShoppingList() {
		this.shoppingList = this.shoppingListService.getShoppingList();
	}

	addArticle(article: Article) {
		this.shoppingList = this.shoppingListService.addArticle(article);
	}

	removeArticle(article: Article) {
		this.shoppingList = this.shoppingListService.removeArticle(article);
	}


}
