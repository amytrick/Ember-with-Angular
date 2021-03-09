import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Album } from "../album";
import { Photo } from "../photo";
import { AlbumService } from '../album.service';
import { SharedPhotosService } from '../shared-photos.service';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-album-details',
  templateUrl: './album-details.component.html',
  styleUrls: ['./album-details.component.css']
})

export class AlbumDetailsComponent implements OnInit {

  album: Album = <Album>{};
  photos: Photo[] = [];
  new_name: string = "";
  album_name: string = "";
  hidden = true;

  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService,
    private route: ActivatedRoute
  ) {
  }

  getPhotos(album_id: number): void {
    this.albumService.getPhotos(album_id).subscribe(photos => {
      this.sharedPhotosService.updatePhotos(photos);
    });
  }

  getAlbum(id: number): void {
    this.albumService.getAlbum(id)
      .subscribe(album => {
        this.album = album;
        this.album_name = album.name;
      });
    this.sharedPhotosService.setCurrentAlbumId(id);
  }

  renameAlbum(): void {
    console.log(this.new_name)
    this.sharedPhotosService.renameAlbum(this.new_name);
    this.album_name = this.new_name;
  }

  renameToggle() {
    if (this.hidden == true)
      this.hidden = false;
    else
      (this.hidden = true)
    console.log(this.hidden)
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      this.getAlbum(Number(id));
      this.getPhotos(Number(id));
    })

    this.sharedPhotosService.sharedPhotos.subscribe(photos => this.photos = photos);
  }

}
