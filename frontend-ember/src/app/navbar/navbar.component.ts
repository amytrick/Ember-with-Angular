import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { faFilter, faSearch, faEquals, faGreaterThanEqual, faLessThanEqual } from '@fortawesome/free-solid-svg-icons';
import { AlbumService } from '../album.service';
import { SharedPhotosService } from '../shared-photos.service';




@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  faFilter = faFilter;
  faSearch = faSearch;
  equals = faEquals;
  greater = faGreaterThanEqual;
  less = faLessThanEqual;

  currentRating: number = 0;
  currentAlbumId: number = 0;

  public isCollapsed = true;
  equality: string = "";
  testForm = this.fb.group({
    equality: ['', Validators.required]
  });

  searchword: string = "";


  constructor(
    private route: ActivatedRoute,
    private fb: FormBuilder,
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService
  ) {
  }

  display() {
    console.log(this.equality);
  }

  setFilter() {
    console.log(this.currentRating);
    console.log(this.equality);
    this.albumService.setFilter(this.currentRating, this.equality, this.currentAlbumId).subscribe(photos => this.sharedPhotosService.updatePhotos(photos));
  }

  search() {
    console.log(this.searchword);
    this.albumService.search(this.searchword).subscribe(photos => this.sharedPhotosService.updatePhotos(photos));
  }

  ngOnInit(): void {
    this.sharedPhotosService.currentAlbumId.subscribe(albumId => this.currentAlbumId = albumId);
  }

}
