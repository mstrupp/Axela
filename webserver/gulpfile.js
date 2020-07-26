var gulp = require('gulp');

gulp.task('css', function () {
    const postcss = require('gulp-postcss')
  
    return gulp.src('src/tailwind.css')
        .pipe(postcss([
            require('tailwindcss'),
            require('autoprefixer'),
        ]))
        .pipe(gulp.dest('public_html/'))
})

gulp.task('copy-html', function () {
    return gulp.src(['src/*.html', 'src/*.php']).pipe(gulp.dest('public_html'));
})

gulp.task('watch', function() {
    gulp.watch('src/**/*.+(html|php)', gulp.task('copy-html'))
});