import {NgModule} from '@angular/core';
import {MatListModule} from '@angular/material/list';
import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatInputModule} from '@angular/material';
import {MatDialogModule} from '@angular/material/dialog';
import {MatTableModule} from '@angular/material/table';





@NgModule({
    imports: [
        MatListModule,
        MatIconModule,
        MatToolbarModule,
        MatButtonModule,
        MatSelectModule,
        MatGridListModule,
        MatCardModule,
        MatProgressSpinnerModule,
        MatAutocompleteModule,
        MatInputModule,
        MatDialogModule,
        MatTableModule,
    ],
    exports: [
        MatListModule,
        MatIconModule,
        MatToolbarModule,
        MatButtonModule,
        MatSelectModule,
        MatGridListModule,
        MatCardModule,
        MatProgressSpinnerModule,
        MatAutocompleteModule,
        MatInputModule,
        MatDialogModule,
        MatTableModule,
    ]
})

export class MaterialModule { }
