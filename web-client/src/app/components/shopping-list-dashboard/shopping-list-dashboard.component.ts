import { Component, OnInit } from '@angular/core';
import { Article } from '../../models/article';
import { ArticlesService } from '../../services/articles.service';
import { Category } from '../../models/category';

@Component({
  selector: 'app-shopping-list-dashboard',
  templateUrl: './shopping-list-dashboard.component.html',
  styleUrls: ['./shopping-list-dashboard.component.css']
})
export class ShoppingListDashboardComponent implements OnInit {

  articles: Article[];
  categories: Category[];

  constructor(private articlesService: ArticlesService) { }

  ngOnInit() {
    this.getArticles();
    this.getCategories();
  }

  getArticles() {
    this.articlesService.getArticles().subscribe(data => {
        this.articles = data;
    })
  }

  getCategories() {
    this.articlesService.getCategories().subscribe(data => {
        this.categories = data;
    })
  }

}
