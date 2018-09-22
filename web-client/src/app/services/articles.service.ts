import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { Article } from '../models/article';
import { Category } from '../models/category';
import { SubCategory } from '../models/subcategory';
import { environment } from '../../environments/environment'



@Injectable({
  providedIn: 'root'
})
export class ArticlesService {

    articles = [];
    categories = [];
    subcategories = [];

    private articlesUrl = environment.serverUrl;


    httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
    };

    constructor(
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

    getSubCategories(categoriId: string): Observable<Category[]> {
        const url = this.articlesUrl + 'subcategories'
        let options = this.httpOptions;
        options['search'] = categoriId;

        return this.http.post<SubCategory[]>(url, options)
            .pipe(
                tap(subcategories => this.log('fetched subcategories')),
                catchError(this.handleError('getSubCategories', []))
            );
    }


    getFilteredArticles(search: {}): Observable<Article[]>{
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
        console.log('ArticleService: '+ message);
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
