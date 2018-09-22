import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AppComponent} from './app.component';
import {ArticleDetailComponent} from './components/article-detail/article-detail.component';
import {ArticleComponent} from './components/article/article.component';
import {HomeComponent} from './components/home/home.component';
import {ProjectInfoComponent} from './components/project-info/project-info.component';
import {UserComponent} from './components/user/user.component';
import { ShoppingListDashboardComponent } from './components/shopping-list-dashboard/shopping-list-dashboard.component';

const routes: Routes = [
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent},
    {path: 'articles', component: ShoppingListDashboardComponent},
    {path: 'info', component: ProjectInfoComponent},
    {path: 'user', component: UserComponent},
    // { path: 'detail/:id', component: HeroDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]


})
export class AppRoutingModule { }
