import {NgModule} from '@angular/core';
import {MatListModule} from '@angular/material/list';
import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';



@NgModule({
    imports: [
        MatListModule,
        MatIconModule,
        MatToolbarModule,
        MatButtonModule,
    ],
    exports: [
        MatListModule,
        MatIconModule,
        MatToolbarModule,
        MatButtonModule,
    ]
})

export class MaterialModule { }
