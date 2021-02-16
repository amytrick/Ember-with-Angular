import { Component, OnInit } from '@angular/core';
import { Album } from "../album";
import { Photo } from "../photo";

import { AlbumService } from '../album.service';


@Component({
  selector: 'app-album-details',
  templateUrl: './album-details.component.html',
  styleUrls: ['./album-details.component.css']
})
export class AlbumDetailsComponent implements OnInit {

  album?: Album;
  photos?: Photo[];
  constructor(private albumService: AlbumService) { }

  getPhotos(album_id: number): void {
    this.albumService.getPhotos(album_id).subscribe(photos => this.photos = photos);
  }

  getAlbum(album_id: number): void {
    this.albumService.getAlbum(album_id).subscribe(album => this.album = album);
  }

  ngOnInit(): void {
    this.getAlbum(1/*albumId*/);
    this.getPhotos(1/*albumId*/);
  }
}
