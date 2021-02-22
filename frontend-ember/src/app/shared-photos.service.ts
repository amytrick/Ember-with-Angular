import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { ReplaySubject } from 'rxjs';

import { Photo } from './photo';


@Injectable({
  providedIn: 'root'
})
export class SharedPhotosService {
  private photos = new BehaviorSubject<Photo[]>([]);
  sharedPhotos = this.photos.asObservable();

  private message = new BehaviorSubject('First Message');
  sharedMessage = this.message.asObservable();


  constructor() {
    console.log("SharedPhotosService got constructed");
  }

  updatePhotos(photos: Photo[]) {
    console.log("Beep bop update photos in service")
    this.photos.next(photos);
  }

  nextMessage(message: string) {
    this.message.next(message)
  }


}
