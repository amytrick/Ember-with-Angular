import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Album } from '../album';
import { SharedPhotosService } from '../shared-photos.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums: Album[] = [];
  public isCollapsed = true;
  newAlbumName: string = "NEW ALBUM NAME";
  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService
  ) { }

  getAlbums(user_id: number): void {
    this.albumService.getAlbums(user_id).subscribe(albums => this.albums = albums);
  }

  addAlbum() {
    this.albumService.addAlbum(this.newAlbumName, 1 /*userid*/).subscribe(album => this.albums.push(album));
    this.isCollapsed = true;
    this.newAlbumName = "NEW ALBUM NAME";
  }

  ngOnInit(): void {
    this.getAlbums(1/*userId*/);
  }

}
