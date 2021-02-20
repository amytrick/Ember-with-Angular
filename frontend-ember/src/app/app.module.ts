import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumDetailsComponent } from './album-details/album-details.component';
import { PhotoDetailsComponent } from './photo-details/photo-details.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LibraryComponent } from './library/library.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { DragDropDirective } from './drag-drop.directive';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    AlbumsComponent,
    AlbumDetailsComponent,
    PhotoDetailsComponent,
    NavbarComponent,
    LibraryComponent,
    SidebarComponent,
    DragDropDirective
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    NgbModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
