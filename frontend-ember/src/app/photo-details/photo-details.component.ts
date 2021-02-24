import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumService } from '../album.service';
import { Photo } from "../photo";
import { SharedPhotosService } from '../shared-photos.service';

// import { faCoffee } from '@fortawesome/free-solid-svg-icons';
// <fa-icon [icon]="faCoffee"></fa-icon>


@Component({
  selector: 'app-photo-details',
  templateUrl: './photo-details.component.html',
  styleUrls: ['./photo-details.component.css']
})
export class PhotoDetailsComponent implements OnInit {

  photo: Photo = <Photo>{};
  photos: Photo[] = [];
  currentDisplayedIdx: number;

  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService,
    private route: ActivatedRoute
  ) { }

  // getPhoto(id: number): void {
  //   this.albumService.getPhoto(id)
  //     .subscribe(photo => this.photo = photo);
  // }

  previous(): void {
    this.sharedPhotosService.previousPhoto();
  }

  next(): void {
    this.sharedPhotosService.nextPhoto();
  }

  ngOnInit(): void {
    // this.currentDisplayedIdx = +this.route.snapshot.paramMap.get('id');
    // this.getPhoto(this.currentDisplayedIdx);
    this.sharedPhotosService.sharedPhotos.subscribe(photos => this.photos = photos);
    this.sharedPhotosService.currentPhoto.subscribe(photo => this.photo = photo);
  }


}
