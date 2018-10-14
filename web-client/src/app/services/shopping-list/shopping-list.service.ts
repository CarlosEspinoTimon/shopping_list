import { Injectable } from '@angular/core';

import { Article } from '../../models/article';

import { Observable, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ShoppingListService {

    //   shoppingList: Article[] = [];
    shoppingList: [[Article, number]];
    // shoppingListt: [{id: string, article: Article, units: number}] 

    // shoppingListt: [{id: string, article: Article, units: number}] 

    myObservable = of(this.shoppingList);

    constructor() { }

    getShoppingList(): [[Article, number]] {
        return this.shoppingList;
    }

    getObservableList() {
        return this.myObservable;
    }

    addArticle(article: Article, total: number):  [[Article, number]] {
        if (this.shoppingList == null) {
            this.shoppingList = [[article, total]];
            // this.shoppingListt.push({id: String(article.id), article: article, units: total})
        } else {
            if(this.shoppingList.filter(value=> value[0].id==article.id).length > 0) {
                let index = -1;
                let counter = 0;
                while (counter<this.shoppingList.length) {
                    for (let item of this.shoppingList) {
                        if (item[0].id == article.id) {
                            index = counter;
                            counter = this.shoppingList.length
                        }
                        counter += 1
                    }
                }

                this.shoppingList[index][1] = this.shoppingList[index][1] + total
            } else {
                this.shoppingList.push([article, total]);
            }
            
        }
        return this.shoppingList;
    }

    removeArticle(article: Article, total: number):  [[Article, number]] {
        var index = -1;
        var counter = 0;
        while (counter<this.shoppingList.length) {
            for (let item of this.shoppingList) {
                if (item[0].id == article.id) {
                    index = counter;
                    counter = this.shoppingList.length
                }
                counter += 1
            }
        }
        if (total>=this.shoppingList[index][1]) {
            this.shoppingList.splice(index, 1);
        } else {
            this.shoppingList[index][1] = this.shoppingList[index][1] - total
        }
        
        return this.shoppingList;
    }

}
