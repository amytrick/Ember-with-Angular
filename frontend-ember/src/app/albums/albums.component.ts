import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Album } from '../album';

import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
// import { faPlus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  // faPlus = faPlus;
  albums: Album[] = [];

  constructor(private albumService: AlbumService) { }

  getAlbums(user_id: number): void {
    this.albumService.getAlbums(user_id).subscribe(albums => this.albums = albums);
  }

  // openVerticallyCentered(content) {
  //   this.modalService.open(content, { centered: true });
  // }

  ngOnInit(): void {
    this.getAlbums(1/*userId*/);
  }

}
