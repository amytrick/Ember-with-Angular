import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumService } from '../album.service';
import { Photo } from "../photo";
import { SharedPhotosService } from '../shared-photos.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-photo-details',
  templateUrl: './photo-details.component.html',
  styleUrls: ['./photo-details.component.css']
})
export class PhotoDetailsComponent implements OnInit {

  photo: Photo = <Photo>{};
  photos: Photo[] = [];
  currentDisplayedIdx: number;
  subscription: Subscription;
  message: string;

  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService,
    private route: ActivatedRoute
  ) { }

  getPhoto(id: number): void {
    this.albumService.getPhoto(id)
      .subscribe(photo => this.photo = photo);

  }

  previous(): void {
    this.currentDisplayedIdx -= 1;
  }

  next(): void {
    this.sharedPhotosService.nextMessage("Second Message");
  }

  ngOnInit(): void {
    console.log("PhotoDetailsComponent onInit called");
    this.currentDisplayedIdx = +this.route.snapshot.paramMap.get('id');

    this.getPhoto(this.currentDisplayedIdx);

    this.sharedPhotosService.sharedMessage.subscribe(message => this.message = message);
    this.subscription = this.sharedPhotosService.sharedPhotos.subscribe(photos => this.photos = photos);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
