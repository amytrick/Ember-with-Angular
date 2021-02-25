import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Album } from '../album';

@Component({
  selector: 'app-add-to-album',
  templateUrl: './add-to-album.component.html',
  styleUrls: ['./add-to-album.component.css']
})
export class AddToAlbumComponent implements OnInit {

  albums: Album[] = [];
  public isCollapsed = true;

  constructor(private albumService: AlbumService) { }

  getAlbums(user_id: number): void {
    this.albumService.getAlbums(user_id).subscribe(albums => this.albums = albums);
  }

  ngOnInit(): void {
    this.getAlbums(1/*userId*/);
  }

}
