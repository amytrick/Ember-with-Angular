import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumDetailsComponent } from './album-details/album-details.component';
import { PhotoDetailsComponent } from './photo-details/photo-details.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LibraryComponent } from './library/library.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { TagsComponent } from './tags/tags.component';
import { GalleryComponent } from './gallery/gallery.component';
import { RatingsComponent } from './ratings/ratings.component';
import { AddToAlbumComponent } from './add-to-album/add-to-album.component';
import { RatingComponent } from './rating/rating.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';

import { UploadPhotoComponent } from './upload-photo/upload-photo.component';
import { CloudinaryModule } from '@cloudinary/angular-5.x';
import * as  Cloudinary from 'cloudinary-core';

import { ToastrModule } from 'ngx-toastr';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginPageComponent } from './login-page/login-page.component';


@NgModule({
  declarations: [
    AppComponent,
    AlbumsComponent,
    AlbumDetailsComponent,
    PhotoDetailsComponent,
    NavbarComponent,
    LibraryComponent,
    SidebarComponent,
    TagsComponent,
    GalleryComponent,
    RatingsComponent,
    AddToAlbumComponent,
    RatingComponent,
    UploadPhotoComponent,
    LoginPageComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FontAwesomeModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(),
    CloudinaryModule.forRoot(Cloudinary, { cloud_name: 'dv77rliti' })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
