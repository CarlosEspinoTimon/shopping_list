import { Injectable } from '@angular/core';

import { Article } from '../../models/article';


@Injectable({
  providedIn: 'root'
})
export class ShoppingListService {

  shoppingList: Article[] = [];

  constructor() { }

  getShoppingList(): Article[] {
	  return this.shoppingList;
  }

  addArticle(article: Article): Article[] {
	  this.shoppingList.push(article);
	  return this.shoppingList;
  }

  removeArticle(article: Article) {
	  var index = this.shoppingList.indexOf(article, 0);
	  if (index > -1) {
		  this.shoppingList.splice(index, 1);
	  }
	  return this.shoppingList;
  }

}
