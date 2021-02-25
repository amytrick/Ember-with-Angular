import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { faFilter, faSearch, faEquals, faGreaterThanEqual, faLessThanEqual } from '@fortawesome/free-solid-svg-icons';


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
  public isCollapsed = true;


  constructor(private route: ActivatedRoute,) { }

  ngOnInit(): void {
  }

}
