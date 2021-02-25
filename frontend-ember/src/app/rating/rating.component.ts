import { Component, OnInit } from '@angular/core';
import { SharedPhotosService } from '../shared-photos.service';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})
export class RatingComponent implements OnInit {
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
