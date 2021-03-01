import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

import { Photo } from './photo';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root'
})
export class SharedPhotosService {
  private photos = new BehaviorSubject<Photo[]>([]);
  sharedPhotos = this.photos.asObservable();

  private photo = new BehaviorSubject<Photo>(<Photo>{});
  currentPhoto = this.photo.asObservable();

  private currentIdx: any = 0
  private has_current_photo: boolean = false;
  constructor(private http: HttpClient) {
  }

  private resetCurrentPhoto() {
    this.photo.next(<Photo>{});
    this.has_current_photo = false;
  }

  updateCurrentRating(newRating: number): void {
    if (this.has_current_photo) {
      this.photo.value.rating = newRating;
      this.http.post(`${API_URL}/update-rating`, { photo_id: this.photo.value.photo_id, rating: newRating }).subscribe();
    }
  }

  nextPhoto() {
    this.currentIdx = (this.currentIdx + 1) % this.photos.value.length;
    this.photo.next(this.photos.value[this.currentIdx]);
  }

  previousPhoto() {
    this.currentIdx = (this.currentIdx == 0) ? this.photos.value.length - 1 : this.currentIdx - 1;
    this.photo.next(this.photos.value[this.currentIdx]);
  }

  setPhoto(photo_id: number) {
    this.currentIdx = this.photos.value.findIndex(photo => photo.photo_id == photo_id);
    this.photo.next(this.photos.value[this.currentIdx]);
    this.has_current_photo = true;
  }

  updatePhotos(photos: Photo[]) {
    this.photos.next(photos);
    this.resetCurrentPhoto();
  }

  addToAlbum(album_id: number) {
    console.log(`shared ${album_id}, not yet made the API call `);
    this.http.post(`${API_URL}/add-to-album`, { photo_id: this.photo.value.photo_id, album_id: album_id }).subscribe();

  }
}
