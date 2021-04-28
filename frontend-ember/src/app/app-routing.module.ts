import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AlbumDetailsComponent } from './album-details/album-details.component';
import { PhotoDetailsComponent } from './photo-details/photo-details.component';
import { LibraryComponent } from './library/library.component';
import { LoginPageComponent } from './login-page/login-page.component';

const routes: Routes = [
  { path: 'library', component: LibraryComponent },
  { path: 'album/:id', component: AlbumDetailsComponent },
  { path: 'photo', component: PhotoDetailsComponent },
  { path: 'login', component: LoginPageComponent },

  // search/rating
  // search/tag
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
