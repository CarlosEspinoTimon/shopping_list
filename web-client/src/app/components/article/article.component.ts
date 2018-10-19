import { Component, Inject} from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material';

import { Article } from '../../models/article';


@Component({
  selector: 'app-articles',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent {

    article: Article;

    constructor(
        @Inject(MAT_DIALOG_DATA) public data: Article,
        ) {}
    

}
