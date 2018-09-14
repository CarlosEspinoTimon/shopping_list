import { Component, OnInit } from '@angular/core';
import { Article } from '../../models/article';
import { ArticlesService } from '../../services/articles.service';
import { Category } from '../../models/category';
import { Observable } from 'rxjs';
import { ShoppingListService } from '../../services/shopping-list/shopping-list.service';

@Component({
  selector: 'app-shopping-list-dashboard',
  templateUrl: './shopping-list-dashboard.component.html',
  styleUrls: ['./shopping-list-dashboard.component.css']
})
export class ShoppingListDashboardComponent implements OnInit {

  articles: Article[];
  categories: Category[];
  shoppingList: Article[];

  constructor(
    private articlesService: ArticlesService,
    private shoppingListService: ShoppingListService
  ) { }

  ngOnInit() {
    this.getArticles();
    this.getCategories();
  }

  noArticles(): boolean {
    let emptyArticles: Article[];
    return this.articles == emptyArticles;
  }

  getArticles() {
    this.articlesService.getArticles().subscribe(data => {
        this.articles = data;
    });
  };

  getCategories() {
    this.articlesService.getCategories().subscribe(data => {
        this.categories = data;
    });
  };

  getFilteredArticles(search: string) {
    this.articlesService.getFilteredArticles(search)
        .subscribe(data => {
          this.articles = data;
        });
  };

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
