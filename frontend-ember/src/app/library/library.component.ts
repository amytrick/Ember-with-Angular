import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Photo } from "../photo";

@Component({
  selector: 'app-library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.css']
})
export class LibraryComponent implements OnInit {

  photos?: Photo[];

  constructor(private albumService: AlbumService) { }

  fillLibrary(user_id: number): void {
    this.albumService.fillLibrary(user_id).subscribe(photos => this.photos = photos);
  }

  ngOnInit(): void {
    this.fillLibrary(1);
  }

}
