import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

    public constructor(private titleService: Title) { }

    ngOnInit() {
        this.setTitle("Cheaper Shopping")
    }

    public setTitle(newTitle: string) {
        this.titleService.setTitle(newTitle)
    }

}
