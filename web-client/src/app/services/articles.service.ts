import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Article } from '../models/article';
import { Category } from '../models/category';
import { MessageService } from './message.service';
import { URLSearchParams } from 'url';



@Injectable({
  providedIn: 'root'
})
export class ArticlesService {

    articles = [];
    categories = [];

    private articlesUrl = 'http://localhost:5000/shopping_list/api/';
    private articlesUrl2 = 'http://localhost:5000/shopping_list/api/1';

    httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
    };

    constructor(
        private messageService: MessageService,
        private http: HttpClient
    ) { }

    getArticles(): Observable<Article[]> {
        return this.http.get<Article[]>(this.articlesUrl+'articles')
            .pipe(
                tap(articles => this.log('fetched articles')),
                catchError(this.handleError('getArticles', []))
            );
    }

    getCategories(): Observable<Category[]> {
        return this.http.get<Category[]>(this.articlesUrl+'categories')
            .pipe(
                tap(categories => this.log('fetched categories')),
                catchError(this.handleError('getCategories', []))
            );
    }


    getFilteredArticles(search: string): Observable<Article[]>{
        const url = this.articlesUrl + 'filtered_articles'
        let options = this.httpOptions;
        options['search'] = search;
  
        return this.http.post<Article[]>(url, options)
            .pipe(
                tap(articles => this.log('fetched filtered articles')),
                catchError(this.handleError('getFilteredArticles', []))
            );
    }

    private log(message: string) {
        this.messageService.add('ArticleService: ' + message);
    }

    /**
     * Handle Http operation that failed.
     * Let the app continue.
     * @param operation - name of the operation that failed
     * @param result - optional value to return as the observable result
     */
    private handleError<T> (operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {

        // TODO: send the error to remote logging infrastructure
        console.error(error); // log to console instead

        // TODO: better job of transforming error for user consumption
        this.log(`${operation} failed: ${error.message}`);

        // Let the app keep running by returning an empty result.
        return of(result as T);
        };
    }

}
