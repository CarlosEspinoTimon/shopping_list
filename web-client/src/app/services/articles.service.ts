import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Article } from '../models/article';
import { MessageService } from './message.service';


@Injectable({
  providedIn: 'root'
})
export class ArticlesService {

    articles = [];

    private articlesUrl = 'http://localhost:5000/shopping_list/api/articles';

    httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
    };

    constructor(
        private messageService: MessageService,
        private http: HttpClient
    ) { }

    getArticles(): Observable<Article[]> {
        return this.http.get<Article[]>(this.articlesUrl)
            .pipe(
                tap(articles => this.log('fetched articles')),
                catchError(this.handleError('getArticles', []))
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
