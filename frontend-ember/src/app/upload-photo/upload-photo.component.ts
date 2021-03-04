import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';

@Component({
  selector: 'app-upload-photo',
  templateUrl: './upload-photo.component.html',
  styleUrls: ['./upload-photo.component.css']
})
export class UploadPhotoComponent implements OnInit {
  photo: any;

  constructor(private albumService: AlbumService) { }

  uploadPhoto() {
    console.log(this.photo);
    this.albumService.uploadPhoto(this.photo);
  }

  ngOnInit(): void {
  }

}
