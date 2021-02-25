import { Component, OnInit } from '@angular/core';
import { SharedPhotosService } from '../shared-photos.service';

@Component({
  selector: 'app-ratings',
  templateUrl: './ratings.component.html',
  styleUrls: ['./ratings.component.css']
})
export class RatingsComponent implements OnInit {
  currentRate = 3;
  constructor(private sharedPhotosService: SharedPhotosService,
  ) { }

  updateRating(newRating: number) {
    this.sharedPhotosService.updateCurrentRating(newRating);
  }

  ngOnInit(): void {
    this.sharedPhotosService.currentPhoto.subscribe(photo => this.currentRate = photo.rating);
  }

}
