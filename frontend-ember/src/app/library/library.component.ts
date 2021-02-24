import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { SharedPhotosService } from '../shared-photos.service';

@Component({
  selector: 'app-library',
  templateUrl: './library.component.html',
  styleUrls: ['./library.component.css']
})
export class LibraryComponent implements OnInit {

  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService,
  ) { }

  fillLibrary(user_id: number): void {
    this.albumService.fillLibrary(user_id).subscribe(photos => {
      this.sharedPhotosService.updatePhotos(photos);
    });
  }

  ngOnInit(): void {
    this.fillLibrary(1);
  }

}
