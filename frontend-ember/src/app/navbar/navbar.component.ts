import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';
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

  currentRating: number = 0;

  public isCollapsed = true;
  equality: string = "";
  testForm = this.fb.group({
    equality: ['', Validators.required]
  });


  constructor(private route: ActivatedRoute, private fb: FormBuilder) {
  }

  display() {
    console.log(this.equality);
  }

  setFilter() {
    console.log(this.currentRating);
    console.log(this.equality);
  }

  ngOnInit(): void {
  }

}
