import {NgModule} from '@angular/core';
import {MatListModule} from '@angular/material/list';
import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatGridListModule} from '@angular/material/grid-list';






@NgModule({
    imports: [
        MatListModule,
        MatIconModule,
        MatToolbarModule,
        MatButtonModule,
        MatSelectModule,
        MatGridListModule,
    ],
    exports: [
        MatListModule,
        MatIconModule,
        MatToolbarModule,
        MatButtonModule,
        MatSelectModule,
        MatGridListModule,
    ]
})

export class MaterialModule { }
