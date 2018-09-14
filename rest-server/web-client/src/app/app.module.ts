import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ArticleDetailComponent } from './components/article-detail/article-detail.component';
import { ArticleComponent } from './components/article/article.component';
import { MessagesComponent } from './components/messages/messages.component';

import { MaterialModule } from './materials/materials';
import { AppRoutingModule } from './/app-routing.module';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { HomeComponent } from './components/home/home.component';
import { ProjectInfoComponent } from './components/project-info/project-info.component';
import { UserComponent } from './components/user/user.component';
import { ShoppingListDashboardComponent } from './components/shopping-list-dashboard/shopping-list-dashboard.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    ArticleDetailComponent,
    ArticleComponent,
    MessagesComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    ProjectInfoComponent,
    UserComponent,
    ShoppingListDashboardComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    MaterialModule,
    AppRoutingModule,
    NgbModule.forRoot()
  ],
  exports: [
      MaterialModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
