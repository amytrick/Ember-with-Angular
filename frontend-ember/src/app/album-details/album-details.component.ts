import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Album } from "../album";
import { Photo } from "../photo";
import { AlbumService } from '../album.service';
import { SharedPhotosService } from '../shared-photos.service';

@Component({
  selector: 'app-album-details',
  templateUrl: './album-details.component.html',
  styleUrls: ['./album-details.component.css']
})

export class AlbumDetailsComponent implements OnInit {

  album: Album = <Album>{};
  photos: Photo[] = [];

  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService,
    private route: ActivatedRoute
  ) { }

  getPhotos(album_id: number): void {
    this.albumService.getPhotos(album_id).subscribe(photos => {
      this.sharedPhotosService.updatePhotos(photos);
    });
  }

  getAlbum(id: number): void {
    this.albumService.getAlbum(id)
      .subscribe(album => this.album = album);
  }

  ngOnInit(): void {

    const id = +this.route.snapshot.paramMap.get('id');
    this.getAlbum(id)
    this.getPhotos(id);
    this.sharedPhotosService.sharedPhotos.subscribe(photos => this.photos = photos);
  }

}
