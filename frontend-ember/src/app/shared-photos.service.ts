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

  currentIdx: any = 0

  constructor(private http: HttpClient) {
  }

  updateCurrentRating(newRating: number) {
    this.photo.value.rating = newRating;
    this.http.post<Number>(`${API_URL}/update-rating`, { photo_id: this.photo.value.photo_id, rating: newRating }).subscribe(data => { });
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
  }

  updatePhotos(photos: Photo[]) {
    this.photos.next(photos);
  }
}
