import { Injectable } from '@angular/core';
import { SESSION_STORAGE, StorageService } from 'angular-webstorage-service';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';

import { environment } from '../../../environments/environment'

import { User } from '../../models/user'

@Injectable({
  providedIn: 'root'
})
export class UserService {

    private serverUrl = environment.serverUrl;
    httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
    };


    constructor(private http: HttpClient) { }

    register(): Observable<any> {
        return this.http.get<any>(this.serverUrl+'user_registration');
    }

    login(username: string, password: string): Observable<any> {
        return this.http.post<any>(this.serverUrl+'user_login', {
                'username': username, 'password': password})
            .pipe(map(user => {
                // Login succesful if there's a jwt token in the response
                console.log(user)
                if (user.access_token) {
                    console.log(user.access_token)
                }
                if (user && user.access_token) {
                    // Store user details and jwt token in locla storage to keep user logged in between page refreshes
                    localStorage.setItem('currentUser', JSON.stringify(user));
                }
            }));
    }

    isLogged() {
        console.log(localStorage.getItem('currentUser'))
        return localStorage.getItem('currentUser') != null;
    }
}
