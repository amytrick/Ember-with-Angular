import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

import { Photo } from './photo';

@Injectable({
  providedIn: 'root'
})
export class SharedPhotosService {
  private photos = new BehaviorSubject<Photo[]>([]);
  sharedPhotos = this.photos.asObservable();

  constructor() {
  }

  updatePhotos(photos: Photo[]) {
    this.photos.next(photos);
  }
}
