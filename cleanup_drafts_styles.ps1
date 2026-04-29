$files = @{
    "_drafts/src/html/c_courses.html" = @{
        'class="courses-image" style="cursor: pointer;"' = 'class="courses-image cursor-pointer"'
        'class="courses-detail" style="cursor: pointer;"' = 'class="courses-detail cursor-pointer"'
        'a style="cursor: pointer;" data-toggle="modal" data-target="#scheduleModal"' = 'a class="cursor-pointer" data-toggle="modal" data-target="#scheduleModal"'
        '<span style="background-color:#AD8A56;" class="badge">' = '<span class="badge badge-olive">'
        '<span style="background-color:#C9B037;" class="badge">' = '<span class="badge badge-gold">'
        '<span style="background-color:#D7D7D7;" class="badge">' = '<span class="badge badge-silver">'
    }
    "_drafts/src/html/apply.html" = @{
        '<span style="background-color:#C9B037;" class="badge">' = '<span class="badge badge-gold">'
        '<span style="background-color:#C9B037;"class="badge">' = '<span class="badge badge-gold">'
        '<span style="background-color:#AF9500;"  class="badge">' = '<span class="badge badge-blue">'
        '<span style="background-color:#AF9500;" class="badge">' = '<span class="badge badge-blue">'
        '<span  style="background-color:#D7D7D7;" class="badge">' = '<span class="badge badge-silver">'
        '<span style="background-color:#D7D7D7;"  class="badge ">' = '<span class="badge badge-silver">'
        '<span style="background-color:#D7D7D7;" class="badge">' = '<span class="badge badge-silver">'
        '<span style="background-color:#AD8A56;" class="badge">' = '<span class="badge badge-olive">'
    }
    "_drafts/src/html/menu.html" = @{
        '<img src="images/CEIT_Logo_70X70.png" style="position: absolute; padding-left: 20px;" alt="">' = '<img src="images/CEIT_Logo_70X70.png" class="position-absolute pl-20" alt="">'
    }
    "_drafts/dest/index.html" = @{
        'href="https://github.com/ceit-png/ceit-png.github.io/raw/master/Brochure.pdf" target="_blank" style="font-size: 12px;"' = 'href="https://github.com/ceit-png/ceit-png.github.io/raw/master/Brochure.pdf" target="_blank" class="font-12"'
        'style="padding-left:76px"' = 'class="pl-76"'
        'style="padding-left: 76px"' = 'class="pl-76"'
        'style="padding-top: 15px;"' = 'class="pt-15"'
        'style="padding-top: 0px"' = 'class="pt-0"'
        'style="width: 100%" class="img-responsive"' = 'class="img-responsive full-width"'
        'a style="cursor: pointer;" data-toggle="modal" data-target="#scheduleModal"' = 'a class="cursor-pointer" data-toggle="modal" data-target="#scheduleModal"'
        'a style="cursor: pointer;" data-toggle="modal" data-target="#CC' = 'a class="cursor-pointer" data-toggle="modal" data-target="#CC'
        'div class="courses-image" style="cursor: pointer;"' = 'div class="courses-image cursor-pointer"'
        'div class="courses-detail" style="cursor: pointer;"' = 'div class="courses-detail cursor-pointer"'
        '<span style="background-color:#AD8A56;" class="badge">' = '<span class="badge badge-olive">'
        '<span style="background-color:#C9B037;" class="badge">' = '<span class="badge badge-gold">'
        '<span style="background-color:#D7D7D7;" class="badge">' = '<span class="badge badge-silver">'
        '<span style="background-color:#AF9500;" class="badge">' = '<span class="badge badge-blue">'
        'h4 style="color:white;">' = 'h4 class="text-white">'
        'a class="submit-btn form-control" href="https://forms.gle/2QmeSHFxHvXBnzLA9" target="_blank" style="padding-top: 15px;">' = 'a class="submit-btn form-control pt-15" href="https://forms.gle/2QmeSHFxHvXBnzLA9" target="_blank">'
    }
}

foreach ($file in $files.Keys) {
    $text = Get-Content -Path $file -Raw
    foreach ($pattern in $files[$file].Keys) {
        $replacement = $files[$file][$pattern]
        $text = $text -replace [regex]::Escape($pattern), $replacement
    }
    Set-Content -Path $file -Value $text -Encoding utf8
}
