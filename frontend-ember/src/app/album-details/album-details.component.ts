import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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

  constructor(
    private albumService: AlbumService,
    private route: ActivatedRoute,
  ) { }

  getPhotos(album_id: number): void {
    this.albumService.getPhotos(album_id).subscribe(photos => this.photos = photos);
  }

  // getPhotos(): void {
  //   const album_id = +this.route.snapshot.paramMap.get('album_id');
  //   this.albumService.getPhotos(album_id)
  //     .subscribe(photos => this.photos = photos);
  // }

  // getAlbum(album_id: number): void {
  //   const album_id = +this.route.snapshot.paramMap.get('album_id');
  //   this.albumService.getAlbum(album_id).subscribe(album => this.album = album);
  // }

  getAlbum(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.albumService.getAlbum(id)
      .subscribe(album => this.album = album);
  }

  ngOnInit(): void {
    this.getAlbum()
    // (1/*albumId*/);
    this.getPhotos(1/*albumId*/);
  }
}
