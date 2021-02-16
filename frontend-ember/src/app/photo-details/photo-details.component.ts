import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Photo } from "../photo";

@Component({
  selector: 'app-photo-details',
  templateUrl: './photo-details.component.html',
  styleUrls: ['./photo-details.component.css']
})
export class PhotoDetailsComponent implements OnInit {

  photo?: Photo;

  constructor(private albumService: AlbumService) { }

  getPhoto(photo_id: number): void {
    this.albumService.getPhoto(photo_id).subscribe(photo => this.photo = photo);
  }

  ngOnInit(): void {
    this.getPhoto(1)
  }

}
