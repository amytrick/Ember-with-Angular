import { Component, OnInit } from '@angular/core';

import { AlbumService } from '../album.service';
import { Album } from '../album';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {

  albums: Album[] = [];

  constructor(private albumService: AlbumService) { }

  getAlbums(user_id: number): void {
    this.albumService.getAlbums(user_id).subscribe(albums => this.albums = albums);
  }

  ngOnInit(): void {
    this.getAlbums(1/*userId*/);
  }

}
