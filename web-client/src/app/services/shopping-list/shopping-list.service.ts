import { Injectable } from '@angular/core';

import { Article } from '../../models/article';



@Injectable({
  providedIn: 'root'
})
export class ShoppingListService {

    shoppingList: [[Article, number]];

    constructor() { }

    /** Function that returns the shopping list */
    getShoppingList(): [[Article, number]] {
        return this.shoppingList;
    }

    /** Function that adds a new article (or more units) */
    addArticle(article: Article, total: number):  [[Article, number]] {
        if (this.shoppingList == null) {
            this.shoppingList = [[article, total]];
        } else {
            // Check wheter the article is already in the list to add more elements, or is new
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

    /** Function that removes an article (or some units) */
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
        // Check wheter there is still units left or all are removed from the list
        if (total>=this.shoppingList[index][1]) {
            this.shoppingList.splice(index, 1);
        } else {
            this.shoppingList[index][1] = this.shoppingList[index][1] - total
        }
        
        return this.shoppingList;
    }

}
