import { Component, OnInit } from '@angular/core';
import { SharedPhotosService } from '../shared-photos.service';
import { Photo } from "../photo";

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.css']
})
export class GalleryComponent implements OnInit {
  photos: Photo[] = [];

  constructor(private sharedPhotosService: SharedPhotosService) { }

  setPhoto(id: number) {
    this.sharedPhotosService.setPhoto(id);
  }

  ngOnInit(): void {
    this.sharedPhotosService.sharedPhotos.subscribe(photos => this.photos = photos);
  }

}
