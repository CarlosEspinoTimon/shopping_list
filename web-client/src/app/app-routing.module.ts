import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
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
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]


})
export class AppRoutingModule { }
