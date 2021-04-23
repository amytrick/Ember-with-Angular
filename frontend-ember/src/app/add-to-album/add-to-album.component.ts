import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Album } from '../album';
import { SharedPhotosService } from '../shared-photos.service';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-add-to-album',
  templateUrl: './add-to-album.component.html',
  styleUrls: ['./add-to-album.component.css']
})
export class AddToAlbumComponent implements OnInit {

  albums: Album[] = [];
  public isCollapsed = true;

  constructor(
    private albumService: AlbumService,
    private sharedPhotoService: SharedPhotosService,
    private toastr: ToastrService) { }

  getAlbums(user_id: number): void {
    this.albumService.getAlbums(user_id).subscribe(albums => this.albums = albums);
  }

  addToAlbum(album_id: number): void {
    this.sharedPhotoService.addToAlbum(album_id);
    this.isCollapsed = true;
    console.log("clicked album title")
    let album_name = this.getAlbumName(album_id)
    this.toastr.success('Success!', `Photo added to ${album_name}`);
  }

  getAlbumName(album_id: number): string {
    for (let album of this.albums) {
      if (album.album_id == album_id) {
        return album.name;
      }
    }
    return "";
  }


  ngOnInit(): void {
    this.getAlbums(1/*userId*/);

  }

}
