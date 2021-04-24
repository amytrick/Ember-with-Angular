import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import * as _ from 'lodash';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-upload-photo',
  templateUrl: './upload-photo.component.html',
  styleUrls: ['./upload-photo.component.css']
})
export class UploadPhotoComponent implements OnInit {
  photo: any;
  cardImageBase64: any;
  isImageSaved: any;

  constructor(private albumService: AlbumService,
    private toasterService: ToastrService) { }

  fileChangeEvent(fileInput: any) {
    console.log('Second upload button pressed');
    console.log(fileInput)
    const reader = new FileReader();
    reader.onload = (e: any) => {
      const image = new Image();
      image.src = e.target.result;
      image.onload = rs => {
        const imgBase64Path = e.target.result;
        console.log(e.target);
        this.cardImageBase64 = imgBase64Path;
        this.isImageSaved = true;
        this.uploadPhoto();
      };
    };
    reader.readAsDataURL(fileInput.target.files[0]);
  }

  uploadPhoto() {
    this.toasterService.info('...uploading');

    this.albumService.uploadPhoto(this.cardImageBase64).subscribe((response) => {
      console.log(response);
      this.toasterService.success('Success', 'Photo uploaded');
    });
  }

  ngOnInit(): void {
  }

}
