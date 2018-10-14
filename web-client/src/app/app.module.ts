import { BrowserModule, Title } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgModule, LOCALE_ID } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ArticleComponent } from './components/article/article.component';

import { MaterialModule } from './materials/materials';
import { AppRoutingModule } from './/app-routing.module';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { HomeComponent } from './components/home/home.component';
import { ProjectInfoComponent } from './components/project-info/project-info.component';
import { UserComponent } from './components/user/user.component';
import { ShoppingListDashboardComponent } from './components/shopping-list-dashboard/shopping-list-dashboard.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import es from '@angular/common/locales/es';
import { registerLocaleData } from '@angular/common';

registerLocaleData(es);

@NgModule({
    declarations: [
        AppComponent,
        ArticleComponent,
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
        ReactiveFormsModule,
        HttpClientModule,
        MaterialModule,
        AppRoutingModule,
        NgbModule.forRoot(),
    ],
    exports: [
        MaterialModule,
    ],
    entryComponents: [
        ArticleComponent,
    ],
    providers: [
        Title,
        {
            provide: LOCALE_ID,
            useValue: 'es-ES',
        },
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }

