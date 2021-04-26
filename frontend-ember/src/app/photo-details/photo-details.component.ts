import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumService } from '../album.service';
import { Photo } from "../photo";
import { SharedPhotosService } from '../shared-photos.service';

import { faTrashAlt, faChevronRight, faChevronLeft } from '@fortawesome/free-solid-svg-icons';



@Component({
  selector: 'app-photo-details',
  templateUrl: './photo-details.component.html',
  styleUrls: ['./photo-details.component.css']
})
export class PhotoDetailsComponent implements OnInit {

  photo: Photo = <Photo>{};
  photos: Photo[] = [];
  currentDisplayedIdx: number;
  faTrashAlt = faTrashAlt;
  faChevronRight = faChevronRight;
  faChevronLeft = faChevronLeft;

  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService,
    private route: ActivatedRoute,
    private _router: Router
  ) { }

  previous(): void {
    this.sharedPhotosService.previousPhoto();
  }

  next(): void {
    this.sharedPhotosService.nextPhoto();
  }

  deletePhoto(): void {
    this.sharedPhotosService.deletePhoto().subscribe(() => {
      this._router.navigate(['library']);
    }
    );
  }

  ngOnInit(): void {
    this.sharedPhotosService.sharedPhotos.subscribe(photos => this.photos = photos);
    this.sharedPhotosService.currentPhoto.subscribe(photo => this.photo = photo);
  }


}
