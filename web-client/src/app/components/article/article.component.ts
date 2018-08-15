import { Component, OnInit } from '@angular/core';
import { Observable, of } from 'rxjs';


import { Article } from '../../models/article';
import { ArticlesService } from '../../services/articles.service';

@Component({
  selector: 'app-articles',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

    // article: Article = {
    //     id: 1,
    //     name: 'Fresitaaas',
    //     price: 5.5,
    //     format: 'Bandeja',
    //     category_id: 1,
    //     sub_category_id: 2,
    //     supermarket_id: 1
    // }

    articles: Article[];

    constructor(private articlesService: ArticlesService) { }

    ngOnInit() {
      this.getArticles();
    }

    getArticles() {
        this.articlesService.getArticles().subscribe(data => {
            this.articles = data;
        })
    }

    // getArticles(): Observable<Article[]> {
    //     this.articlesService.getArticles().subscribe(data => {
    //         this.articles = data;
    //     })
    // }



    // add(name: string): void {
    //     name = name.trim();
    //     if (!name) { return; }
    //     this.articlesService.addArticle({ name } as Hero)
    //       .subscribe(hero => {
    //       this.heroes.push(hero);
    //       });
    //   }
    //
    // delete(hero: Hero): void {
    //     this.heroes = this.heroes.filter(h => h !== hero);
    //     this.articlesService.deleteArticle(hero).subscribe();
    // }

  // constructor() { }
  //
  // ngOnInit() {
  // }

}
