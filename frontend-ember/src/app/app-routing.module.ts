import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumDetailsComponent } from './album-details/album-details.component';
import { PhotoDetailsComponent } from './photo-details/photo-details.component';


const routes: Routes = [
  { path: '', component: AlbumsComponent },
  { path: 'album/:id', component: AlbumDetailsComponent },
  { path: 'photo/:id', component: PhotoDetailsComponent }
  // album/album_id
  // photo/photo_id
  // search/rating
  // search/tag
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
